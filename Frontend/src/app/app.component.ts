import {Component} from '@angular/core';
import * as data from '../../../data.json';
import {Post} from './models/post.interface';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  posts: Post[] = (data as any).default;

  constructor() {}

}
