# xmlExtractor

1. Downloads the xml from given link

2. From the xml, parses through to the first download link whose file_type is DLTINS and download the zip

3. Extract the xml from the zip.

4. Convert the contents of the xml into a CSV with the following header:

    FinInstrmGnlAttrbts.Id
    
    FinInstrmGnlAttrbts.FullNm
    
    FinInstrmGnlAttrbts.ClssfctnTp
    
    FinInstrmGnlAttrbts.CmmdtyDerivInd
    
    FinInstrmGnlAttrbts.NtnlCcy
    
    Issr

5. Store the csv from step 4) in an AWS S3 bucket
