import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DataService } from '../data.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'w2m';
  email='';
  password='';
  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    const dataToSend = { /* Your data object */ };
    this.dataService.sendData(this.email,this.password).subscribe((response: any) => {
      console.log(response); // Handle the response from the API
    });
  }
  /*constructor(private router: Router) { }

  ngOnInit(): void {
  }
  //routing functions if needed*/
}