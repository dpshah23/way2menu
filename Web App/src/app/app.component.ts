import { Component, OnInit } from '@angular/core';
//import { Router } from '@angular/router';
import { DataService } from '../app/data.service';
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
    const dataToSend = {email:this.email,password:this.password};
    this.dataService.sendData(dataToSend).subscribe(response => {
      console.log(response); // Handle the response from the API
    });
  }
  /*constructor(private router: Router) { }

  ngOnInit(): void {
  }
  //routing functions if needed*/
}