/* Program to recover deleted JPEG. 
 * Use JPEG signature 0xff 0xd8 0xff 0xe[[:alnum:]] 
 * Use 512 Bytes range and FAT format 
 * Store every found jpeg in separate files 
 * Name of files : xxx.jpg 
 * return error if wrong number of cli args or unreadeable file */

/* Pseudo-code : 
* - open raw file 
* - repeat until end of file
* - read 512 bytes into a buffer
*   + start o new jpg ?
*   + already found a jpg ?
* - close anyfile
* - keep count of jpg file to name them */

/* if (buffer[0] == 0xff
 *      buffer[1] == 0xd8
 *      buffer[2] == 0xff
 *      (buffer[3] & 0xf0) == 0xe0) */


#include <stdio.h>
// include stdint to have more int definition
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Wrong cli argument.\nUsage : ./revover file_name\n");
        return 1;
    }

    FILE *raw = fopen(argv[1], "r");

    // check availability of file
    if (raw == NULL)
    {
        fprintf(stderr, "Unable to read the file \"%s\", sorry.\n", argv[1]);
        return 2;
    }

    // read 512 bytes blocks and store them to buffer
    // use unsigned integer 8 bits = 1 byte
    uint8_t buffer[512] = {} ;
    int count = 0 ;
    int byte_count = 0 ;
    int jpg_found = 0 ;
    char filename[50] ;
    FILE *img = NULL ;

    // use fread(destination, size, number, source)
    // fread return number of elements read
    // loop while fread read one element. If return 0, it's end of file
    while (fread(buffer, 512, 1, raw) != 0)
    {
        // define easy read int for complicated search
        int jpg_search = (int)(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0);
        /* if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) */
        if (jpg_search)
        {
            // increment count iot create filename
            count ++ ;
            // specify the name depending of the number of jpg found
            sprintf(filename, "%03i.jpg", count);
            // open a file to write
            img = fopen(filename, "w");
            fwrite(buffer, 512, 1, img);
            // close the file after write
            /* fclose(img); */

            // alert that jpg is found
            jpg_found = 1 ;
        // write end of picture when jpg found
        } else if (jpg_found == 1)
        {
            fwrite(buffer, 512, 1, img);
        }

        // store datas if jpg previoulsy found

        byte_count ++ ;
    }
    // print if all bytes has been checked
    printf("%i bytes investigated, %i jpeg found !\n", byte_count * 512, count);
    printf("Pictures found and stored, backup next time...\n");
    fclose(raw);
    return 0;
}
