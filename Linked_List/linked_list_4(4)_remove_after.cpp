#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 어떤 노드의 다음 노드 삭제하는 함수
// prev가 가리키는 노드의 다음 노드를 삭제한다.
Node * remove_after(Node *prev){
  Node *tmp = prev->next;
  if (tmp == NULL){
    return NULL;
  }
  else{
    prev->next = tmp->next;
    return tmp;
  }
}
/* 단순연결리스트에 어떤 노드를 삭제할 때는 삭제할 노드의 바로 앞 노드의 주소가 필요하다. 삭제할 노드의 주소만으로는 삭제할 수 없다. */
