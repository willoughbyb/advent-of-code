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

//let memory = "".Split(',') |> Array.map int
let memory = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,79,14,225,1101,17,42,225,2,74,69,224,1001,224,-5733,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1002,191,83,224,1001,224,-2407,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,18,64,225,1102,63,22,225,1101,31,91,225,1001,65,26,224,101,-44,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,101,78,13,224,101,-157,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,102,87,187,224,101,-4698,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,79,85,224,101,-6715,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,43,46,224,101,-89,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1101,54,12,225,1102,29,54,225,1,17,217,224,101,-37,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1102,20,53,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,1002,223,2,223,1006,224,329,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,344,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,404,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,449,1001,223,1,223,1008,226,677,224,102,2,223,223,1006,224,464,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,479,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,524,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,584,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,599,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,644,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,659,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226".Split(',') |> Array.map int
//let memory = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".Split(',') |> Array.map int

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
