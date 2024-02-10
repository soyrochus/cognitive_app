import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';


@Component({
  selector: 'app-message-input',
  standalone: true,
  templateUrl: './message-input.component.html',
  styleUrls: ['./message-input.component.scss'],
  imports: [FormsModule, MatFormFieldModule, MatInputModule, MatButtonModule]
})

export class MessageInputComponent {
  message: string = '';

  sendMessage() {
    console.log(this.message);
    this.message = ''; // Clear input after sending
  }
}
