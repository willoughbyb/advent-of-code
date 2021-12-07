let isSixDigits pass =
     pass > 99999 && pass < 1000000

let rec containsDoubleDigits (pass:string) =
    if pass.Length >= 2 then
        let char1 = pass.[0]
        let char2 = pass.[1]
        if char1 = char2 then true
        else 
            let rest = pass.[1..]
            containsDoubleDigits(rest)
    else false

let rec digitsAlwaysIncrease (pass:string) =
    if pass.Length >= 2 then
        let int1 = int(pass.[0])
        let int2 = int(pass.[1])

        if int2 < int1 then false
        else digitsAlwaysIncrease(pass.[1..])
    else true
     

let passwordIsValid pass =
     isSixDigits pass && containsDoubleDigits(pass.ToString()) && digitsAlwaysIncrease(pass.ToString())

let checkCurrentPassword current =
    if passwordIsValid current
    then Set.empty.Add current
    else Set.empty

let rec findValidPasswords current last =
     Set.union (checkCurrentPassword current) (if current < last then findValidPasswords (current+1) last else Set.empty)

//findValidPasswords 372038 905157 |> Set.count |> printfn "%d"
findValidPasswords 359282 820401 |> Set.count |> printfn "%d"
