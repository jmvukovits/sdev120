start

# A program which opens two files, reads, and merges them in order by customer numbers
    Declarations
        InputFile geraldinesFile
        InputFile gerardsFile
        OutputFile mergedFile
        num geraldineNumber
        string geraldineName
        string geraldineAddress
        num geraldine_size_in_squareFeet
        num gerardNumber
        string gerardName
        string gerardAddress
        num gerard_size_in_squareFeet
        string END_NUM = "0000000"
        string areBothAtEnd = "N"
    getReady()
    while areBothAtEnd <> "Y"
        mergeRecords()
    endwhile
    finishUp()

stop

#The following modules opens both files for reading to prepare for merging

getReady()
    open geraldinesFile "GeralidineCustomers.dat"
    open gerardsFile "GerardCustomers.dat"
    open mergedFile "Customers.dat"
    readGeraldine()
    readGerard()
    checkEnd()
return

readGeraldine()
    input geraldineNumber, geraldineName, geraldineAddress, geraldine_size_in_squareFeet from geraldinesFile
    if eof then
        geraldineNumber = END_NUM
    endif
return

readGerard()
    input gerardNumber, gerardName, gerardAddress, gerard_size_in_squareFeet from gerardsFile
    if eof then
        gerardNumber = END_NUM
    endif
return

checkEnd()
    if geraldineNumber = END_NUM
        if gerardNumber = END_NUM then
            areBothAtEnd = "Y"
        endif
    endif
return

# This module merges the records by customer numbers
mergeRecords()
    if geraldineNumber < gerardNumber then
        output geraldineNumber, geraldineName, geraldineAddress, geraldine_size_in_squareFeet to mergedFile
        readGeraldine()
    else
        output gerardNumber, gerardName, gerardAddress, geraldine_size_in_squareFeet to mergedFile
    endif
    checkEnd()
return

# This module closes the files to prepare for finishing
finishUp()
    close geraldinesFile
    close gerardsFile
    close mergedFile
return
