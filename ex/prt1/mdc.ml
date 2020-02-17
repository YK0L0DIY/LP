let rec mdc a b =
    if a=b then a
    else
        if a > b then mdc (a-b) b
        else mdc a (b-a);;