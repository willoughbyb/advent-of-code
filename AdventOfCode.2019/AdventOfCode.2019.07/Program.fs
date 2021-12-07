open System

type Instruction (memory:int[], address:int, input:int) =
    let code = sprintf "%05d" memory.[address]

    member this.opcode = int code.[3 .. 4]
    member this.modes = [ 
        string code.[2]
        string code.[1]
        string code.[0] ] |> List.map int

    override this.ToString() =
        sprintf "[%03d] %s opcode:%02d modes:%A params:%A" address code this.opcode this.modes this.parameters

    member this.parameters : (int list) =
        match this.opcode with
        | 1 | 2 | 7 | 8 -> 
            memory.[address + 1 .. address + 3] |> Array.toList
        | 3 | 4 ->
            [| memory.[address + 1] |] |> Array.toList
        | 5 | 6 ->
            memory.[address + 1 .. address + 2] |> Array.toList
        | _ -> List.empty

    member this.getparamval index =
        let par = this.parameters.[index]
        match this.modes.[index] with
        | 0 -> memory.[par] // position mode
        | 1 -> par          // immediate mode
        | _ -> 0

    member this.execute =
        match this.opcode with
        | 1 ->
            let parmA = this.getparamval 0
            let parmB = this.getparamval 1
            let dest  = this.parameters.[2]
            let value = parmA + parmB
            printfn "  execute: setting %d to %d" dest value
            Array.set memory dest value
        | 2 ->
            let parmA = this.getparamval 0
            let parmB = this.getparamval 1
            let dest  = this.parameters.[2]
            let value = parmA * parmB
            printfn "  execute: setting %d to %d" dest value
            Array.set memory dest value
        | 3 ->
            printf "opcode 03 requires input > "
            let input = Console.ReadLine() |> int
            let parmA = this.parameters.[0]
            printfn "  execute: setting %d to %d" parmA input
            Array.set memory parmA input
        | 4 ->
            let value = this.getparamval 0
            printfn "  execute: outputting %d" value
        | 7 ->
            let parmA = this.getparamval 0
            let parmB = this.getparamval 1
            let dest  = this.parameters.[2]
            let value =
                match parmA < parmB with
                | true  -> 1
                | false -> 0
            printfn "  compare: %d < %d" parmA parmB
            printfn "  execute: setting %d to %d" dest value
            Array.set memory dest value
        | 8 ->
            let parmA = this.getparamval 0
            let parmB = this.getparamval 1
            let dest  = this.parameters.[2]
            let value =
                match parmA = parmB with
                | true  -> 1
                | false -> 0
            printfn "  compare: %d = %d" parmA parmB
            printfn "  execute: setting %d to %d" dest value
            Array.set memory dest value
        | _ -> ()

    member this.offset =
        match this.opcode with
        | _ -> this.parameters.Length + 1

    member this.newaddress =
        match this.opcode with
        | 5 ->
            let parmA = this.getparamval 0
            let parmB = this.getparamval 1
            printfn "  compare: %d != 0" parmA
            if parmA <> 0 then
                printfn "  execute: setting address to %d" parmB
                parmB
            else -1
        | 6 ->
            let parmA = this.getparamval 0
            let parmB = this.getparamval 1
            printfn "  compare: %d = 0" parmA
            if parmA = 0 then
                printfn "  execute: setting address to %d" parmB
                parmB
            else -1
        | _ -> -1

    member this.running =
        match this.opcode with
        | 99 -> false
        | _  -> true

let memory = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".Split(',') |> Array.map int

let mutable address = 0
let mutable running = true
let mutable output = 0
while running do
    let instruction = Instruction(memory, address, output)
    printfn "%O" instruction

    instruction.execute |> ignore

    let newaddress = instruction.newaddress
    if newaddress > -1 then address <- newaddress
    else address <- address + instruction.offset

    running <- instruction.running

printfn "%A" memory
