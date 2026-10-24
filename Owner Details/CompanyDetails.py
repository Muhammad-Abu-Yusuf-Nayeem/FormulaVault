=BYROW(
  FILTER(b3:b, b3:b<>""), 
  LAMBDA(id,
    IFERROR(TRANSPOSE(
      FILTER(
        k3:k,
        j3:j = id
      )),
      0
    )
  )
)

33	64
41	29
42	27
56	37
68	72
68	72