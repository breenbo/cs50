/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdio.h>
#include <ctype.h> // to use tolower()
#include <stdlib.h>
#include <string.h> // use of strlen() and memset() to initialize trie
#include <math.h> // use of max()

#include "dictionary.h"

// create global tree to store dict and check words
node *root_dict_tree;

// create global wordcount
int wordcount = 0;

/**
 * returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    // create local node iot work in tree without segfault
    node *currentnode = root_dict_tree ;

    // search each char in trie
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        int index = 0;
        // deal with ' stored at the end of dict array
        if (word[i] == 39)
        {
            index = 26;
        }
        else
        {
            // use tolower for case insensitivity for default case
            index = tolower(word[i]) - 97;
        }
        if (currentnode -> children[index] != NULL)
        {
            // char discovered in trie
            currentnode = currentnode -> children[index];
        }
        else 
        {
            // char not discovered : misspelled word
            return false;
        }
    }
    if (currentnode -> is_word == true)
    {
        // correct word discovered
        return true;
    }
    return false;
}

/**
 * loads dictionary into memory. returns true if successful else false.
 */
bool load(const char *dictionary)
{
    // read each word in the dictionnary file
    // store word in word_trie by storing each letter in a node
    // declare if word is complete or not with is_word = true

    // read words in dictionnary
    // open the FILE
    FILE *dict = fopen(dictionary, "r");
    int lettercount = 0; // memory letter to find the lower layer for deleting

    if (dict == NULL)
    {
        return false;
    }

    // initiate the dict_tree
    root_dict_tree = (node*) calloc(1,sizeof(node));

    // set a node to travel in dict_tree
    /* node *currentnode = NULL; */
    node *currentnode = root_dict_tree;

    // read the letters of words in dictionnary dict
    for (int c = fgetc(dict); c!= EOF; c = fgetc(dict))
    {
        if (c == 39)
        {
            c = 26;
        }
        else
        {
            c -= 97;
        }
        if (c + 97 == 10)
        // check if new line symbol = end of word (ascii 10)
        // no need to create and record another node
        // but need to go to root to prepare a new word record
        {
            currentnode -> is_word = true;
            currentnode = root_dict_tree;
            wordcount ++;
            lettercount = 0; // reset lettercount at the end of each word
        } 
        // store ' in end of array
        else
        {
            // if children doesn't exist yet, create it and go to it
            if (!(currentnode -> children[c]))
            {
                // create node next and attribute memory
                currentnode -> children[c] = (node*) calloc(1,sizeof(node));
                // point children[n] to the new created node
                currentnode = currentnode -> children[c];
            }
            // else simply go to next children
            else
            {
            currentnode = currentnode -> children[c];
            lettercount ++ ;
            }
        }
    }

    fclose(dict);

    return true;
}


/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return wordcount;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    /* node *currentnode = root_dict_tree; */
    /* freenode(currentnode); */
    freenode(root_dict_tree);

    return true;
}

//------------------------------
// additional functions
//------------------------------

void freenode(node *tree)
{
    for (int i = 0; i < 27; i++)
    {
        // check if all children are NULL, unless go down one layer
        if (tree -> children[i] != NULL)
        {
            freenode(tree -> children[i]);
        } 
    }
    // free node with all NULL children
    free(tree);
    return;
}
