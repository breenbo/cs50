/* Function to resize uncompressed bmp file.
 * Take 3 argument :
 * - n : ratio of resize
 * - name of input file
 * - name of ouput file */


#include <stdio.h>
#include <stdlib.h>

// include custom structure
#include "bmp.h"


// use cli argument
int main(int argc, char *argv[])
{
    // remember cli paramaters
    if (argc != 4)
    {
        fprintf(stderr, "usage :./resize resize_factor input_file output_file\n");
        return 1;
    }

    // remember cli arguments
    int resize_factor = atoi(argv[1]);

    // test resize factor >= 0
    if (resize_factor <= 0 || resize_factor > 100)
    {
        fprintf(stderr, "Please enter a integer from 1 to 100.\n");
        return 2;
    }

    // remember cli arguments
    char *input_name = argv[2];
    char *output_name = argv[3];

    // check availability of files
    FILE *input_file = fopen(input_name, "r");
    if (input_file == NULL)
    {
        fprintf(stderr, "Unable to open %s.\n", input_name);
        return 3;
    }

    FILE *output_file = fopen(output_name, "w");
    if (output_file == NULL)
    {
        fprintf(stderr, "Unable to write %s.\n", output_name);
        fclose(input_file);
        return 4;
    }

    // read and store BITMAPFILEHEADER with custom structure of bmp.h
    BITMAPFILEHEADER infile_header;
    fread(&infile_header, sizeof(BITMAPFILEHEADER), 1, input_file);

    // read and store BITMAPINFOHEADER with custom structure of bmp.h
    BITMAPINFOHEADER infile_info;
    fread(&infile_info, sizeof(BITMAPINFOHEADER), 1, input_file);

    // check file is 24 bits uncompressed bitmap file
    if (infile_header.bfType != 0x4d42 || infile_info.biBitCount != 24 || infile_info.biCompression != 0)
    {
        // close file and report error
        fclose(input_file);
        fclose(output_file);
        fprintf(stderr, "Wrong file format.\n");
        return 5;
    }

    // determine new variables
    // bfSize : size of bytes of the bitmap file
    // bfSize = biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER)
    // biSizeImage : size in bytes of the image
    // biSizeImage = ((sizeof(RGBTRIPLE) * biWidth) + padding) * abs(biHeight)
    // biHeight : must be negative to have top-down image
    // biWidth

    // find a way to change output file header and info with new variables, without changing the old ones, BEFORE write in "hard" file
    BITMAPFILEHEADER outfile_header = infile_header ;
    BITMAPINFOHEADER outfile_info = infile_info ;

    outfile_info.biHeight = infile_info.biHeight * resize_factor ;
    outfile_info.biWidth = infile_info.biWidth * resize_factor ;
    int out_padding = (4 - (outfile_info.biWidth * sizeof(RGBTRIPLE)) % 4) % 4 ;
    outfile_info.biSizeImage = ((sizeof(RGBTRIPLE) * outfile_info.biWidth) + out_padding) * abs(outfile_info.biHeight) ;
    outfile_header.bfSize = outfile_info.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) ;

    /* file_info.biHeight *= resize_factor ; */
    /* file_info.biWidth *= resize_factor ; */
    /* file_info.biSizeImage = ((sizeof(RGBTRIPLE) * file_info.biWidth) + padding) * abs(file_info.biHeight); */
    /* file_header.bfSize = file_info.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER); */

    printf("Original infile\n height : %i - width : %i\n", infile_info.biHeight, infile_info.biWidth);
    printf("Resized file\n height : %i - width : %i\n", outfile_info.biHeight, outfile_info.biWidth);

    // write output_file header
    fwrite(&outfile_header, sizeof(BITMAPFILEHEADER), 1, output_file);

    // write output info header
    fwrite(&outfile_info, sizeof(BITMAPINFOHEADER), 1, output_file);

    // determine padding for scanlines
    int in_padding = (4 - (infile_info.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // iterate over infile's scanlines
    
    // iterate over infile lines
    for (int i = 0, biHeight = abs(infile_info.biHeight); i < biHeight; i++)
    {
        for (int m = 0; m < resize_factor ; m++)
        {
            // iterate over pixels in infile lines
            for (int j = 0; j < infile_info.biWidth; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, input_file);

                // write RGB triple to outfile, resize_factor times
                for (int k = 0; k < resize_factor; k++)
                {
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, output_file);
                }
            }

            // then add out_padding to output_file
            for (int l = 0; l < out_padding; l++)
            {
                fputc(0x00, output_file);
            }
        
            // go back to the start of line (fseek), only if resize_factor - 1 line
            // for last line, don't go back and continue 
            if (m < resize_factor - 1)
            {
                fseek(input_file, -infile_info.biWidth * sizeof(RGBTRIPLE), SEEK_CUR);
            }
        }
       
        // skip over padding, if any
        fseek(input_file, in_padding, SEEK_CUR);
    }

    // close files
    fclose(input_file);
    fclose(output_file);
    printf("Resize done bro !");
    return 0;
}
