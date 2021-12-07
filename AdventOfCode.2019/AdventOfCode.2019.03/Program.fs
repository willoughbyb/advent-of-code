open System;
open System.IO;

let input = File.ReadAllLines("input.txt")
let inputOne = (Array.get input 0).Split ','
let inputTwo = (Array.get input 1).Split ','
//let inputOne = "R75,D30,R83,U83,L12,D49,R71,U7,L72".Split(',')
//let inputTwo = "U62,R66,U55,R34,D71,R55,D58,R83".Split(',')

let getpath_u (cy:int) (distance:int) (x:int) =
    let path = Array.create distance (0, 0)
    for i = 0 to distance - 1 do Array.set path i (x, cy + i + 1)
    path

let getpath_d (cy:int) (distance:int) (x:int) =
    let path = Array.create distance (0, 0)
    for i = 0 to distance - 1 do Array.set path i (x, cy - i - 1)
    path

let getpath_l (cx:int) (distance:int) (y:int) =
    let path = Array.create distance (0, 0)
    for i = 0 to distance - 1 do Array.set path i (cx - i - 1, y)
    path

let getpath_r (cx:int) (distance:int) (y:int) =
    let path = Array.create distance (0, 0)
    for i = 0 to distance - 1 do Array.set path i (cx + i + 1, y)
    path

let getpath (instructions:string[]) =
    let mutable current = (0, 0)
    let mutable path : (int*int)[] = [| |]

    Array.iter (fun (s) ->
        let len = String.length s
        let direction = s.Substring(0, 1)
        let distance = s.Substring(1, len - 1) |> int

        let (cx, cy) = current
        match direction with
        | "U" ->
            path <- Array.append path (getpath_u cy distance cx)
            current <- (cx, cy + distance)
        | "D" ->
            path <- Array.append path (getpath_d cy distance cx)
            current <- (cx, cy - distance)
        | "L" ->
            path <- Array.append path (getpath_l cx distance cy)
            current <- (cx - distance, cy)
        | "R" ->
            path <- Array.append path (getpath_r cx distance cy)
            current <- (cx + distance, cy)
        | _   -> ()
    ) instructions

    path

let getdistance (point : int*int) =
    Math.Abs(fst point) + Math.Abs(snd point)

let getlength (path : (int * int)[]) (intersection: int * int) =
    let index = Array.findIndex (fun (pathStep) -> pathStep = intersection) path
    index + 1

let path1 = getpath inputOne
let path2 = getpath inputTwo

let intersections = Set.intersect (Set.ofArray path1) (Set.ofArray path2) |> Set.toArray

intersections
    |> Array.map (fun (intersec) -> getdistance intersec)
    |> Array.min
    |> printfn "Smallest Distance: %d"

printfn "Getting path lengths"
let lengths1 = intersections |> Array.map (fun (intersection) -> getlength path1 intersection)
let lengths2 = intersections |> Array.map (fun (intersection) -> getlength path2 intersection)

let lengthTotals = Array.create intersections.Length 0
for i = 0 to intersections.Length - 1 do Array.set lengthTotals i (lengths1.[i] + lengths2.[i])

Array.min lengthTotals |> printfn "Smallest Length %d"
