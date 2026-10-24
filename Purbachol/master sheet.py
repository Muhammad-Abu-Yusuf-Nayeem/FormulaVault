# combines data from  'DataFromWeb Power' and 'DataFromWeb Subkabla', into a single array.  where column X has the value 'Unique'
=VSTACK(
  QUERY('DataFromWeb Power'!C3:X,"SELECT C,D,E,F,G,K,L,M,Q,R,S WHERE X = 'Unique'",0),
  QUERY('DataFromWeb Subkabla'!C3:X,"SELECT C,D,E,F,G,K,L,M,Q,R,S WHERE X = 'Unique'",0)
)
