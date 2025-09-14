export interface Todo {
  id: number;
  content: string;
  is_completed: boolean;
}

export interface TodoCreate {
  content: string;
  is_completed?: boolean;
}

export interface TodoPatch {
  content?: string;
  is_completed?: boolean;
}

export interface TodoCount {
  count: number;
}
