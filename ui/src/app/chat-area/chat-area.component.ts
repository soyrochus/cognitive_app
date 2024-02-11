import { Component } from '@angular/core';
import { MatListModule } from '@angular/material/list';
import { ChatService } from '../chat.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-chat-area',
  standalone: true,
  imports: [MatListModule, CommonModule],
  templateUrl: './chat-area.component.html',
  styleUrl: './chat-area.component.scss'
})
export class ChatAreaComponent {

  messages$ = this.chatService.messages$;

  constructor(private chatService: ChatService) { }
}
