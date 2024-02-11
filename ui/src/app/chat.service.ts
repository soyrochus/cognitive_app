
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private _messages = new BehaviorSubject<string[]>([]);
  public messages$ = this._messages.asObservable();

  addMessage(message: string) {
    this._messages.next([...this._messages.value, message]);
  }
}
