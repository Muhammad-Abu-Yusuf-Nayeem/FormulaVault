=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(b7),
  'Source of truth'!$A$3:$A<=VALUE(b7+99),
  REGEXMATCH('Source of truth'!$C$3:$C,"ওয়েষ্ট")
)),0)