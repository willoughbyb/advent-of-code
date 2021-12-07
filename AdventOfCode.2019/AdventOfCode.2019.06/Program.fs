open System.IO

type Planet = { name: string; mutable children: Planet list }

let rec addTo (root:Planet) (name:string) (childName:string) =
    if root.name = name then
        root.children <- List.append root.children [{ name = childName; children = List.empty }]
    else for child in root.children do addTo child name childName

let rec getDepth (root:Planet) (name:string) (depth:int) =
    if root.name = name then depth
    else root.children
        |> List.map (fun (child) -> getDepth child name depth + 1)
        |> List.sum

let parseTree (lines:string[]) =
    let line = lines.[0].Split(')')

    let root =
        { name = line.[0];
          children = [{ name = line.[1]; children = List.empty }] }

    for i = 1 to lines.Length - 1 do
        let line = lines.[i].Split(')')
        addTo root line.[0] line.[1]

    root

let input = File.ReadAllLines("input.txt")
let root  = parseTree input
let names =
    input
    |> Array.collect (fun (line) -> line.Split(')'))
    |> Array.distinct

printfn "%A" names
printfn "%O" root

names
    |> Array.map (fun (name) -> getDepth root name 1)
    |> Array.sum
    |> printfn "total: %d"