#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 어떤 노드 뒤에 새로운 노드를 삽입하는 함수
// 삽입에 성공하면 1, 아니면 0을 반환한다.
int add_after(Node *prev, char *item){
  if (prev==NULL)
  return 0;

  Node *tmp = (Node *)malloc(sizeof(Node));
  tmp->data = item;
  tmp->next = prev->next;
  prev->next = tmp;

  return 1;
}
/* 연결리스트에 새로운 노드를 삽입할 때 삽입할 위치의 바로 앞 노드의 주소가 필요하다. 
즉 어떤 노드의 뒤에 삽입하는 것은 간단하지만, 반대로 어떤 노드의 앞에 삽입하는 것은 간단하지 않다. */
