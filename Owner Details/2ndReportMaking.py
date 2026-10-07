=IFERROR(SUM(FILTER(
  'Source of truth'!$F$3:$F,
  'Source of truth'!$A$3:$A>=VALUE(b7),
  'Source of truth'!$A$3:$A<=VALUE(b7+99),
  REGEXMATCH('Source of truth'!$C$3:$C,"ওয়েষ্ট")
)),0)


# Logic: Col6 = column F, so only rows where F is not empty will be imported.
=QUERY(
  IMPORTRANGE("https://docs.google.com/spreadsheets/d/1y_RpFYkXAwN3ByT6vTKclnY6mJV93ELiidKmbkpEGsM/edit?gid=652444612#gid=652444612","'Common Ownership Master File'!A6400:F"),
  "SELECT * WHERE Col6 IS NOT NULL",
  0
)