import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'w2m';
  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  login() {
    this.router.navigate(['/login']);
  }
  signup() {
    this.router.navigate(['/signup']);
  }
}



