import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'w2m';
  email='';
  password='';
  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  //routing functions if needed
}



