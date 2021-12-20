#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 연결리스트 순회하기(traverse)
// 연결리스트의 index번째 위치에 새로운 노드를 만들어서 삽입한다.
int add(int index, char *item){
  if (index<0)
    return 0;

  Node *tmp = (Node *)malloc(sizeof(Node));
  tmp->data = item;
  tmp->next = NULL;

  if(index==0){
    add_first(item);
    return 1;
  }

  Node *prev = get_node(index - 1)
  if (prev != NULL){
    add_after(prev, item);
    return 1;
  }
  return 0;
}
