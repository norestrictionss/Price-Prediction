#include<stdio.h>
#include<stdlib.h>


typedef struct LinkedList{
	
	int data;
	struct LinkedList *next;
}LinkedList;




int main(){
	
	
	FILE *fPtr = fopen("sample_input.txt", "r");
	char c;
	int line_num = 1;
	LinkedList *head = (LinkedList*)malloc(sizeof(LinkedList));
	LinkedList *temp = (LinkedList*)malloc(sizeof(LinkedList));
	LinkedList *ptr1 = head;
	int base = 0;
	LinkedList *head2 = (LinkedList*)malloc(sizeof(LinkedList));
	LinkedList *ptr2 = head2;
	
	int base_digit_count = 0;
	while(c != EOF){
		c = fgetc(fPtr);
		if(c =='\n')
			line_num++;
		else{
			if(line_num == 3){
				
				if(base_digit_count==1)
					base = 10;
				else
					base =(int)c -48;
				base_digit_count++;
				
			}
				
			else if(line_num == 1){
				ptr1->data = (int)c -48;
				ptr1->next = (LinkedList*)malloc(sizeof(LinkedList));
				ptr1 = ptr1->next;
				ptr1->next = NULL;
			
			}
			else if(line_num == 2){
				ptr2->data = (int)c -48;
				ptr2->next = (LinkedList*)malloc(sizeof(LinkedList));
				ptr2 = ptr2->next;
				ptr2->next = NULL;
			
			}
		}
	}
	printf("         ");
	while(head->next !=NULL){
		
		printf("%d", head->data);
		head = head->next;
	}
	printf("\n");
	printf("         ");
	while(head2->next !=NULL){
		printf("%d", head2->data);
		head2 = head2->next;
		
	}
	printf("\n");
	printf("x");
	printf("_____________\n");
	printf("%d", base);
	return 0;
}
