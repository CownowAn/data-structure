#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 첫 번째 노드를 삭제하는 함수
// 연결리스트의 첫번째 노드를 삭제하고 그 노드의 주소를 반환한다.
Node * remove_first(){
  if (head==NULL){
    return NULL;
  }
  else{
    Node *tmp = head;
    head = head->next;
    return tmp;
  }
}
