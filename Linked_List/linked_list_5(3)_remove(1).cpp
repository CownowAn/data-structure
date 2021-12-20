#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// index번째 노드를 삭제하고, 그 노드에 저장된 데이터를 반환한다.
Node *remove(int index){
  if (index<0){
    return NULL;
  }

  if (index==0){
    return remove_first();
  }

  Node *prev = get_node(index-1);
  if (prev==NULL)
    return NULL;
  else{
    return remove_after(prev);
  }
}
