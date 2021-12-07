
let input = [|1;12;2;3;1;1;2;3;1;3;4;3;1;5;0;3;2;10;1;19;1;19;6;23;2;13;23;27;1;27;13;31;1;9;31;35;1;35;9;39;1;39;5;43;2;6;43;47;1;47;6;51;2;51;9;55;2;55;13;59;1;59;6;63;1;10;63;67;2;67;9;71;2;6;71;75;1;75;5;79;2;79;10;83;1;5;83;87;2;9;87;91;1;5;91;95;2;13;95;99;1;99;10;103;1;103;2;107;1;107;6;0;99;2;14;0;0;|]

type Instruction(operation:int, arg1:int, arg2:int, destination:int) =
    member this.Operation = operation
    member this.Arg1 = arg1
    member this.Arg2 = arg2
    member this.Destination = destination
    override this.ToString() =
        sprintf "INS: %d %d %d %d" this.Operation this.Arg1 this.Arg2 this.Destination

let parseInstruction (chunk:int[]) =
    new Instruction(chunk.[0], chunk.[1], chunk.[2], chunk.[3])

let parseInstructionShort (chunk:int[]) =
    new Instruction(chunk.[0], 0, 0, 0)

let compute (memory:int[]) (instruction:Instruction) =
    match instruction.Operation with
    | 1 -> memory.[instruction.Arg1] + memory.[instruction.Arg2]
    | 2 -> memory.[instruction.Arg1] * memory.[instruction.Arg2]
    | _ -> -1

for noun in [0..99] do 
    for verb in [0..99] do
        let memory = Array.copy input
        Array.set memory 1 noun
        Array.set memory 2 verb
        printfn "Checking %A" memory.[0..4]

        memory |> Array.chunkBySize 4 |> Array.map (fun (chunk) ->
                match chunk.Length with
                | 4 -> parseInstruction chunk
                | _ -> parseInstructionShort chunk
            )
            |> Array.iter (fun (instruction) ->
                let result = compute memory instruction
                if result > 0 then Array.set memory instruction.Destination result
            )

        let computedValue = memory.[0]
        printfn "  computed value: %d" computedValue
        if computedValue = 19690720 then failwithf "%d" (100 * noun + verb)
