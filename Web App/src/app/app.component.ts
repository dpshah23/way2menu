import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
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
  signup1:boolean=false;
  hide:boolean=false;
  constructor(private dataService: DataService, private router:Router) { }
  ngOnInit(): void {}

  send(){
    this.dataService.send(this.email,this.password).subscribe((result)=>
    (console.warn(result)))
  }
  signup(){
    this.signup1 = true;
    this.hide=!this.hide;
    this.router.navigate(['/signup']);
  }
  //routing functions if needed
  /*ngOnInit(): void {
    const dataToSend = {'email':this.email,'password':this.password};
    this.dataService.sendData(dataToSend).subscribe(response => {
      console.log(response); // Handle the response from the API
    });
  }*/
}
