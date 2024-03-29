import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { ApiService } from '../api.service';
import { ChatService } from '../chat.service';

@Component({
  selector: 'app-message-input',
  standalone: true,
  templateUrl: './message-input.component.html',
  styleUrls: ['./message-input.component.scss'],
  imports: [FormsModule, MatFormFieldModule, MatInputModule, MatButtonModule]
})

export class MessageInputComponent {

  message: string = '';

  constructor(private apiService: ApiService, private chatService: ChatService) { }

  sendMessage() {
    console.log(this.message);
    this.chatService.addMessage(this.message);

    this.apiService.sendPrompt(this.message).subscribe(response => {
       console.log(response);
       this.chatService.addMessage(response);
    })

     // Clear input after sending
    this.message = '';
  }
}

