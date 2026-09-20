# company page -> All RS DAG
=ARRAYFORMULA('All Receiver'!B8:D)

# All Receiver -> company purchase
=ARRAYFORMULA('PAP'!f6:f)
=ARRAYFORMULA('NPL'!f6:f)
=ARRAYFORMULA('SAN'!f6:f)
=ARRAYFORMULA('SPC'!f6:f)
=ARRAYFORMULA('Personal'!f6:f)


// #  common file -> PPP -> ক্রয়কৃত জমি
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!K6:K,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> ক্রমিক নং
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!a6:a,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> পুরাতন অফিস ফাইল নং
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!b6:b,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> নতুন অফিস ফাইল নং
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!c6:c,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> দাতার নাম
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!p6:p,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> মাধ্যমের নাম
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!q6:q,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> গ্রহিতার নাম
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!o6:o,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> দলিল নম্বর
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!m6:m,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)


// #  common file -> PPP -> দলিলের তারিখ
=LET(
  ids, FILTER(D6:D, D6:D<>""),
  CompanyName, 'Common File'!G6:G,
  DagNo, 'Common File'!I6:I,
  DynamicValue, 'Common File'!n6:n,

  BYROW(
    ids,
    LAMBDA(id,
      IFERROR(
        TRANSPOSE(
          FILTER(
            DynamicValue,
            CompanyName="PPP",
            DagNo=id
          )
        ),
        ""
      )
    )
  )
)

