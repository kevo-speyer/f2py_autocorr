#!/bin/python

#BEGIN MAIN PROGRAM
def main(): # main_script
    """
    This routine reads 'drop_fluct.mide', and writes out the time correlation function
    """
    import numpy as np
#    from fort_lib import f_routine as corr_f #Import fortran compiled library
    from fort_lib_intel import f_routine as corr_f
#    from py_corr import corr as corr_py #Import pure python routine
            
    #Read data
    input_file = 'drop_fluct.mide.gz' 
    time = read_data( input_file, 1) 
    x = read_data( input_file, 2)  
    #z = read_data( input_file, 4)  
    
    #Do heavy calculation
    autocorr_x = corr_f(x) # Call fortran routine # As fast as Muhammad Ali
    #autocorr_z = corr_f(z) # INPUT MUST BE A NUMPY ARRAY OF RANK 1
    #autocorr = corr_py(x,n) # python routine, 850 slower than fortran

    #Save data
    save_data('autocorr_drop_fluct_x.mide', autocorr_x, time)
    #save_data('autocorr_drop_fluct_z.mide', autocorr_z, time)

#END MAIN

#BEGIN SUBROUTINES

def save_data(file_name,data_in,fst_col=0):
    """Save data (2nd column) to  file passed as string in first argument. 
    OPTIONAL: If a 3rd argument is passed (must be a numpy array of the same length as data), this will be printed as
    first column. If no 3rd argument is passed, the first column will be 0, 1, 2, ..., n """
    import numpy as np
    n = data_in.shape[0]
    g = open(file_name, 'w+')
    
    if type(fst_col) is int:
        fst_col = range(n)

    for i in range(n):
        s = str(str(fst_col[i])+' '+ str(data_in[i]) + '\n') 
        g.write(s)

    g.close()   


def read_data(file_name,col_nr=1):
    """Read file passed as first argument. 
    Second argument is column number to read. If this argument is not passed, default is first column
    Returns the column read from input file as a numpy array
    """
    import numpy as np
    import gzip
 
    col_nr = col_nr - 1

    data = []
    
    if file_name[len(file_name)-3:len(file_name)] == '.gz':  
        with gzip.open(file_name,'r') as f:
            for line in f:
                data.append( float( line.split()[col_nr] ) )
    else:
        with open(file_name,'r') as f:
            for line in f:
                data.append( float( line.split()[col_nr] ) )
 
    x = np.asarray(data)

    return x

########### END SUBROUTINES ##########

if __name__ == "__main__":
    main()













