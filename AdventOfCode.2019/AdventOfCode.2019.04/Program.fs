open System.Text.RegularExpressions

let hasIncreasingDigits (number:int) =
    let nums = Seq.toList (string number) |> List.map string |> List.map int // going straight to int treated it as char ascii ints

    let rec nextIsMoreOrSame (numList:int list) indexA indexB =
        if indexB >= (numList.Length) then true
        else
            numList.[indexA] <= numList.[indexB] && nextIsMoreOrSame numList (indexA + 1) (indexB + 1)

    nextIsMoreOrSame nums 0 1

let hasDouble (number:int) =
    Regex("(\d)\1").IsMatch (string number)

let hasNoTriple (number:int) =
    let matches =
        Regex.Matches((string number), "(\d)\1+")
        |> Seq.filter (fun (m) -> m.Captures.Count > 0)
        |> Seq.collect (fun (m) -> m.Captures)
        |> Seq.filter (fun (c) -> c.Value.Length = 2)
        |> Seq.toList

    matches.Length > 0

let valids =
    [359282 .. 820401] |> List.filter hasIncreasingDigits
    //|> List.filter hasDouble
    |> List.filter hasNoTriple

printfn "# of valid numbers: %d" valids.Length
printfn "%A" valids
