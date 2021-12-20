#include <stdio.h>

int main() {

  struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
  };

  typedef struct node Node;
  Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

  head = (Node *)malloc(sizeof(Node));
  head->data = "Tuesday";
  head->next = NULL;

  Node *q = (Node *)malloc(sizeof(Node));
  q->data = "Thursday";
  q->next = NULL;
  head->next = q;

  // Tuesday Node 앞에, 즉 연결 리스트 맨 앞에 Monday Node 추가
  q =(Node *)malloc(sizeof(Node));
  q->data = "Monday";
  q->next = head;
  head = q;

  Node *p = head;
  while(p != NULL){
    printf("%s\n", p->data);
    p = p->next;
  }
} 
