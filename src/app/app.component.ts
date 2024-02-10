import { Component } from '@angular/core';
import { SidebarComponent } from './sidebar/sidebar.component';
import { ChatAreaComponent } from './chat-area/chat-area.component';
import { MessageInputComponent } from './message-input/message-input.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports:  [SidebarComponent, ChatAreaComponent, MessageInputComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'cognitive-ui';
}
