import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private API_URL = 'http://localhost:8000'; // Replace with your Python server URL

  constructor(private http: HttpClient) { }

  sendPrompt(data: any): Observable<any> {
    return this.http.post(`${this.API_URL}/prompt`, data);
  }
}
