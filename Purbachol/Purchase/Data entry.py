// Sheet Names
const FORM_SHEET = "Data Entry Form";
const DATA_SHEET = "Master Sheet";

// Array of all input cell locations in columns D and H
const INPUT_CELLS = [
  "D5",  // পুরাতন ফাইল নং
  "D7",  // নতুন ফাইল নং
  "D9",  // মৌজা
  "D11",  // থানা
  "D15",  // দলিলের ধরণ
  "D17",  // গ্রহিতা কোঃ নাম
  "D19", // দলিল নম্বর
  "D21", // দলিলের তারিখ
  "D25", // আর.এস খতিয়ান
  "H25", // এস.এ খতিয়ান
  "D27", // আর.এস দাগ
  "H27", // এস.এ দাগ
  "D29", // ক্রয়কৃত জমি (শতাংশ)
  "H29", // দাগে মোট জমি (শতাংশ)
  "D33", // দাতার নাম
  "D35", // গ্রহিতার নাম
  "D37"  // মাধ্যমের নাম
];

/**
 * Submits form data to 'Master Sheet' matching header sequence
 */
function submitData() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const formSheet = ss.getSheetByName(FORM_SHEET);
  const dataSheet = ss.getSheetByName(DATA_SHEET);
  
  if (!formSheet || !dataSheet) {
    SpreadsheetApp.getUi().alert("Error: Sheet tab names do not match!");
    return;
  }

  // Generate Auto-increment Serial Number (ক্রমিক নং)
  const lastRow = dataSheet.getLastRow();
  const nextSlNo = lastRow > 1 ? dataSheet.getRange(lastRow, 1).getValue() + 1 : 1;

  // Retrieve values from form fields in D and H columns
  const puratonFile = formSheet.getRange("D5").getValue();
  const notunFile = formSheet.getRange("D7").getValue();
  const mouza = formSheet.getRange("D9").getValue();
  const thana = formSheet.getRange("D11").getValue();
  const dolilDhoron = formSheet.getRange("D15").getValue();
  const grohitaCoName = formSheet.getRange("D17").getValue();
  const dolilNo = formSheet.getRange("D19").getValue();
  const dolilTarikh = formSheet.getRange("D21").getValue();
  const rsKhotian = formSheet.getRange("D25").getValue();
  const saKhotian = formSheet.getRange("H25").getValue();
  const rsDag = formSheet.getRange("D27").getValue();
  const saDag = formSheet.getRange("H27").getValue();
  const kroyJomi = formSheet.getRange("D29").getValue();
  const motJomi = formSheet.getRange("H29").getValue();
  const datarName = formSheet.getRange("D33").getValue();
  const grohitarName = formSheet.getRange("D35").getValue();
  const madhyamerName = formSheet.getRange("D37").getValue();

  // Basic validation check
  if (!puratonFile && !notunFile && !dolilNo) {
    SpreadsheetApp.getUi().alert("Please enter data in the form before submitting.");
    return;
  }

  // Map values to match Master Sheet column headers (A to R)
  const rowData = [
    nextSlNo,         // Col A: ক্রমিক নং
    puratonFile,      // Col B: পুরাতন অফিস ফাইল নং
    notunFile,        // Col C: নতুন অফিস ফাইল নং
    mouza,            // Col D: মৌজা
    thana,            // Col E: থানা
    dolilDhoron,      // Col F: দলিলের ধরণ
    grohitaCoName,    // Col G: গ্রহিতা কোঃ নাম
    saKhotian,        // Col H: এস.এ খতিয়ান
    rsKhotian,        // Col I: আর.এস খতিয়ান
    saDag,            // Col J: এস.এ দাগ
    rsDag,            // Col K: আর.এস দাগ
    motJomi,          // Col L: দাগে মোট জমি
    kroyJomi,         // Col M: ক্রয়কৃত জমি (শতাংশ)
    dolilNo,          // Col N: দলিল নম্বর
    dolilTarikh,      // Col O: দলিলের তারিখ
    grohitarName,     // Col P: গ্রহিতার নাম
    datarName,        // Col Q: দাতার নাম
    madhyamerName     // Col R: মাধ্যমের নাম
  ];

  // Append entry to Master Sheet
  dataSheet.appendRow(rowData);

  // Clear entry form fields
  clearForm();

  SpreadsheetApp.getUi().alert("Data successfully added to Master Sheet!");
}

/**
 * Resets all entry input fields
 */
function clearForm() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const formSheet = ss.getSheetByName(FORM_SHEET);

  INPUT_CELLS.forEach(cell => {
    formSheet.getRange(cell).clearContent();
  });
}