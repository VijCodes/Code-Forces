let is_palindrome s =
    let rec aux i j =
        if i >= j then true
        else if s.[i] <> s.[j] then false
        else aux (i + 1) (j - 1)
    in
    aux 0 (String.length s - 1)
;;

(* Example usage *)
let () =
    if is_palindrome "racecar" then
        print_endline "It's a palindrome!"
    else
        print_endline "It's not a palindrome."