#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 연결리스트에 데이터들이 오름차순으로 정렬되어 있다는 가정하에서 새로운 데이터를 삽입한다.
void add_to_ordered_list(char *item){
  Node *p = head;
  Node *q = NULL;
  while (p!=NULL && strcmp(p->data, item)<=0){
    q = p;
    p = p->next;
  }
  if (q==NULL)
    add_first(item);
  else
    add_after(q); 
}
