open System.IO

let width  = 3
let height = 2

let countOf (number:int) (layer:int list) =
    layer |> List.filter (fun num -> num = number) |> List.length

let input = 
    File.ReadAllLines("input.txt")
    |> Array.toList
    |> List.collect (fun line -> [for c in line -> c.ToString()])
    |> List.map (fun num -> int num)
    |> List.chunkBySize (width * height)

// print input
printfn "Input:"
input
|> List.iter (fun slice ->
    slice.[0 .. width - 1] |> List.iter (fun i -> printf "%d" i)
    printfn ""
)

let index = 
    input
    |> List.mapi (fun i layer -> (i, (countOf 0 layer)))
    |> List.minBy (fun tuple -> snd tuple)
    |> fst

printfn "%d" ((countOf 1 input.[index]) * (countOf 2 input.[index]))

let layerCount = (List.length input) - 1

let graph =
    [0 .. layerCount]
    |> List.map (fun i ->
        [0 .. (width * height) - 1] |> List.map (fun j -> input.[i].[j])
    )

// print graph
printfn "Graph:"
graph
|> List.iter (fun slice ->
    slice.[0 .. width - 1] |> List.iter (fun i -> printf "%d" i)
    printfn ""
)

let image =
    graph
    |> List.map (fun slice -> 
        slice |> List.filter (fun i -> i < 2) |> List.head
    )

image
|> List.chunkBySize width
|> List.iter (fun (line) ->
    line |> List.iter (fun i -> 
        //printf "%d" i
        match i with
        | 0 -> printf "█"
        | _ -> printf " "
    )
    printfn ""
)

(*
0011111000101011100011101
0100111011011011011100100
0110100010010000010101111
1000010110000101110101110
*)