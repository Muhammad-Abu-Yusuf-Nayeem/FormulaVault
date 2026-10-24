=BYROW(
  FILTER(A6:A, A6:A<>""), 
  LAMBDA(id,
    IFERROR(TRANSPOSE(
      FILTER(
        'Source of truth'!$f$3:$f,
        'Source of truth'!$A$3:$A = id
      )),
      0
    )
  )
)



=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1kRUvEOyo22Z2yWP2Akly7MnludaYobWqXBV5La1a0zw/edit?gid=147110446#gid=147110446","'Individual'!a538:p847")

=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1kRUvEOyo22Z2yWP2Akly7MnludaYobWqXBV5La1a0zw/edit?gid=147110446#gid=147110446","'Individual'!a1080:p1472")

=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1kRUvEOyo22Z2yWP2Akly7MnludaYobWqXBV5La1a0zw/edit?gid=147110446#gid=147110446","'Individual'!a2144:p2422")

=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1kRUvEOyo22Z2yWP2Akly7MnludaYobWqXBV5La1a0zw/edit?gid=147110446#gid=147110446","'Individual'!a3412:p3470")

=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1kRUvEOyo22Z2yWP2Akly7MnludaYobWqXBV5La1a0zw/edit?gid=147110446#gid=147110446","'Individual'!a3568:p3608")





















=REDUCE(
  "",
  FILTER(A6:A,A6:A<>""),
  LAMBDA(acc,id,
    IF(
      acc="",
      IFERROR(
        TOROW(
          FILTER(
            'Source of truth'!B3:F,
            'Source of truth'!A3:A=id
          ),
          0,
          FALSE
        ),
        ""
      ),
      VSTACK(
        acc,
        IFERROR(
          TOROW(
            FILTER(
              'Source of truth'!B3:F,
              'Source of truth'!A3:A=id
            ),
            0,
            FALSE
          ),
          ""
        )
      )
    )
  )
)