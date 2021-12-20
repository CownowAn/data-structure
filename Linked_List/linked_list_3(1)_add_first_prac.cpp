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

  // 연결 리스트 맨 앞에 "Ann"을 추가하려고 한다.
  Node *tmp = (Node *)malloc(sizeof(Node));
  tmp->data = "Ann";
  tmp->next = head;
  head = tmp;
  /* 연결 리스트를 다루는 프로그램에서 가장 주의할 점은 내가 작성한 코드가 일반적인 경우만이 아니라 특수한 경우에도 문제 없이 작동하는지 확인하는 것이다. 
  이 경우에는 기존의 연결 리스트의 길이가 0인 경우, 즉 head가 NULL인 경우에도 문제가 없는지 확인해야 한다. 확인해보면, 
  "Ann" Node의 link field는 NULL을 가리키게 되고 head는 "Ann" Node를 가리키게 되므로 문제 없다. */
} 
