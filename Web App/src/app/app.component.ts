import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'w2m';
  welcome="Welcome to WAY 2 MENU";
  static isButtonVisible = true;
  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  login() {
    this.welcome="";
    AppComponent.isButtonVisible=false;
    this.router.navigate(['/login']);
  }
  signup() {
    this.welcome="";
    AppComponent.isButtonVisible=false;
    this.router.navigate(['/signup']);
  }
  get isButtonVisible() {
    return AppComponent.isButtonVisible;
  }
}



