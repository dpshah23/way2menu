import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'w2m';
  welcome="Welcome to"+"<br>"+"WAY 2 MENU";
  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  login() {
    this.welcome="";
    this.router.navigate(['/login']);
  }
  signup() {
    this.welcome="";
    this.router.navigate(['/signup']);
  }
}



