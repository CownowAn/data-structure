#include <stdio.h>

int main() {

  struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
  };

  typedef struct node Node;
  Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

  head = (Node *)malloc(sizeof(Node));
  head->data = "Tom";
  head->next = NULL;

  Node *q1 = (Node *)malloc(sizeof(Node));
  q1->data = "Dick";
  q1->next = NULL;
  head->next = q1;

  Node *q2 = (Node *)malloc(sizeof(Node));
  q2->data = "Harry";
  q2->next = NULL;
  q1->next = q2;

  // "Dick" Node (prev 지금은 q1 Node)뒤에 새로운 "Jim" Node 를 삽입하려고 한다.
  Node *tmp = (Node *)malloc(sizeof(Node));
  tmp->data = "Jim"; // data_to_store;
  tmp->next = q1->next; // prev->next;
  q1->next = tmp; 
} 
