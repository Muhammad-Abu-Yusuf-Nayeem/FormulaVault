=HSTACK('Individual 1164 Bigha'!V6:V, 'Individual 1164 Bigha'!G6:G, 'Individual 1164 Bigha'!W6:W, 'Individual 1164 Bigha'!H6:H, 'Individual 1164 Bigha'!X6:X, 'Individual 1164 Bigha'!I6:I, 'Individual 1164 Bigha'!Y6:Y, 'Individual 1164 Bigha'!J6:J, 'Individual 1164 Bigha'!Z6:Z, 'Individual 1164 Bigha'!K6:K, 'Individual 1164 Bigha'!AA6:AA, 'Individual 1164 Bigha'!L6:L, 'Individual 1164 Bigha'!AB6:AB, 'Individual 1164 Bigha'!M6:M, 'Individual 1164 Bigha'!AC6:AC, 'Individual 1164 Bigha'!N6:N, 'Individual 1164 Bigha'!AD6:AD, 'Individual 1164 Bigha'!O6:O, 'Individual 1164 Bigha'!AE6:AE, 'Individual 1164 Bigha'!P6:P, 'Individual 1164 Bigha'!AF6:AF, 'Individual 1164 Bigha'!Q6:Q, 'Individual 1164 Bigha'!AG6:AG, 'Individual 1164 Bigha'!R6:R, 'Individual 1164 Bigha'!AH6:AH, 'Individual 1164 Bigha'!S6:S, 'Individual 1164 Bigha'!AI6:AI, 'Individual 1164 Bigha'!T6:T, 'Individual 1164 Bigha'!AJ6:AJ, 'Individual 1164 Bigha'!U6:U)


=HSTACK('Individual 1164 Bigha'!V6:V, 'Individual 1164 Bigha'!G6:G, 'Individual 1164 Bigha'!W6:W, 'Individual 1164 Bigha'!H6:H, 'Individual 1164 Bigha'!X6:X, 'Individual 1164 Bigha'!I6:I, 'Individual 1164 Bigha'!Y6:Y, 'Individual 1164 Bigha'!J6:J, 'Individual 1164 Bigha'!Z6:Z, 'Individual 1164 Bigha'!K6:K, 'Individual 1164 Bigha'!AA6:AA, 'Individual 1164 Bigha'!L6:L, 'Individual 1164 Bigha'!AB6:AB, 'Individual 1164 Bigha'!M6:M, 'Individual 1164 Bigha'!AC6:AC, 'Individual 1164 Bigha'!N6:N, 'Individual 1164 Bigha'!AD6:AD, 'Individual 1164 Bigha'!O6:O, 'Individual 1164 Bigha'!AE6:AE, 'Individual 1164 Bigha'!P6:P, 'Individual 1164 Bigha'!AF6:AF, 'Individual 1164 Bigha'!Q6:Q, 'Individual 1164 Bigha'!AG6:AG, 'Individual 1164 Bigha'!R6:R, 'Individual 1164 Bigha'!AH6:AH, 'Individual 1164 Bigha'!S6:S, 'Individual 1164 Bigha'!AI6:AI, 'Individual'!T6:T, 'Individual'!AJ6:AJ, 'Individual'!U6:U)

function protectAllSheetsExceptOwnerAndMe() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheets = ss.getSheets();
  const me = Session.getEffectiveUser(); // The email running the script
  const owner = ss.getOwner();           // The spreadsheet owner

  sheets.forEach(sheet => {
    // 1. Remove any existing protections on this sheet to start fresh
    const existingProtections = sheet.getProtections(SpreadsheetApp.ProtectionType.SHEET);
    existingProtections.forEach(protection => protection.remove());

    // 2. Create a new sheet-level protection
    const protection = sheet.protect().setDescription('Protected: Owner and Editor Only');

    // 3. Remove all current editors from the protection restriction
    protection.removeEditors(protection.getEditors());

    // 4. Explicitly add only the running user and the Owner (if available)
    if (owner) {
      protection.addEditor(owner);
    }
    protection.addEditor(me);

    // 5. Ensure domain-level permission isn't overriding protection
    if (protection.canDomainEdit()) {
      protection.setDomainEdit(false);
    }
  });

  SpreadsheetApp.getUi().alert('All tabs have been successfully protected!');
}