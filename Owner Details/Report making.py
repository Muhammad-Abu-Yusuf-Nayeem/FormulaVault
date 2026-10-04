=VSTACK(
  QUERY('impFrom1.PPP'!C3:Z, "SELECT C, V, W, X, Y, Z WHERE V IS NOT NULL AND Z IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:AE, "SELECT C, AA, AB, AC, AD, AE WHERE AA IS NOT NULL AND AE IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:AJ, "SELECT C, AF, AG, AH, AI, AJ WHERE AF IS NOT NULL AND AJ IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:AO, "SELECT C, AK, AL, AM, AN, AO WHERE AK IS NOT NULL AND AO IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:AT, "SELECT C, AP, AQ, AR, AS, AT WHERE AP IS NOT NULL AND AT IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:AY, "SELECT C, AU, AV, AW, AX, AY WHERE AU IS NOT NULL AND AY IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:BD, "SELECT C, AZ, BA, BB, BC, BD WHERE AZ IS NOT NULL AND BD IS NOT NULL", 0),
  QUERY('impFrom1.PPP'!C3:BI, "SELECT C, BE, BF, BG, BH, BI WHERE BE IS NOT NULL AND BI IS NOT NULL", 0)
)

=VSTACK(
  QUERY('impFromDraftCompany'!C3:S,  "SELECT C, O, P, Q, R, S WHERE O IS NOT NULL AND S IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:X,  "SELECT C, T, U, V, W, X WHERE T IS NOT NULL AND X IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:AC, "SELECT C, Y, Z, AA, AB, AC WHERE Y IS NOT NULL AND AC IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:AH, "SELECT C, AD, AE, AF, AG, AH WHERE AD IS NOT NULL AND AH IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:AM, "SELECT C, AI, AJ, AK, AL, AM WHERE AI IS NOT NULL AND AM IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:AR, "SELECT C, AN, AO, AP, AQ, AR WHERE AN IS NOT NULL AND AR IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:AW, "SELECT C, AS, AT, AU, AV, AW WHERE AS IS NOT NULL AND AW IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:BB, "SELECT C, AX, AY, AZ, BA, BB WHERE AX IS NOT NULL AND BB IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:BG, "SELECT C, BC, BD, BE, BF, BG WHERE BC IS NOT NULL AND BG IS NOT NULL", 0),
  QUERY('impFromDraftCompany'!C3:BL, "SELECT C, BH, BI, BJ, BK, BL WHERE BH IS NOT NULL AND BL IS NOT NULL", 0)
)

=VSTACK(
  QUERY('impFromDraftIndividual'!C3:S,  "SELECT C, O, P, Q, R, S WHERE O IS NOT NULL AND S IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:X,  "SELECT C, T, U, V, W, X WHERE T IS NOT NULL AND X IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:AC, "SELECT C, Y, Z, AA, AB, AC WHERE Y IS NOT NULL AND AC IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:AH, "SELECT C, AD, AE, AF, AG, AH WHERE AD IS NOT NULL AND AH IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:AM, "SELECT C, AI, AJ, AK, AL, AM WHERE AI IS NOT NULL AND AM IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:AR, "SELECT C, AN, AO, AP, AQ, AR WHERE AN IS NOT NULL AND AR IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:AW, "SELECT C, AS, AT, AU, AV, AW WHERE AS IS NOT NULL AND AW IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:BB, "SELECT C, AX, AY, AZ, BA, BB WHERE AX IS NOT NULL AND BB IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:BG, "SELECT C, BC, BD, BE, BF, BG WHERE BC IS NOT NULL AND BG IS NOT NULL", 0),
  QUERY('impFromDraftIndividual'!C3:BL, "SELECT C, BH, BI, BJ, BK, BL WHERE BH IS NOT NULL AND BL IS NOT NULL", 0)
)


=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"প্রবাসী")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"ওয়েষ্ট")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"ইউ এস")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"পুলিশ")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"পূর্বায়ন")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"এফ.*আই")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  REGEXMATCH('Source of truth'!$C$3:$C,"ফ্যাশন")
)),0)
=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,1))),
  'Source of truth'!$A$3:$A<=VALUE(TRIM(INDEX(SPLIT(B6,"-"),1,2))),
  NOT(REGEXMATCH(
    'Source of truth'!$C$3:$C,
    "প্রবাসী|ওয়েষ্ট|ইউ এস|পুলিশ|পূর্বায়ন|এফ আই|ফ্যাশন"
  ))
)),0)

