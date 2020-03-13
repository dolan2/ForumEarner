import {Component, Input, OnInit} from '@angular/core';
import {Post} from "../../models/post.interface";
import {HorizontalBar} from "../../models/horizontal-bar.interface";

@Component({
  selector: 'app-horizontal-bar',
  templateUrl: './horizontal-bar.component.html',
  styleUrls: ['./horizontal-bar.component.css']
})
export class HorizontalBarComponent implements OnInit {

  @Input() posts: Post[];
  data: HorizontalBar[];
  selectData: string[] = ['Age', 'Stack', 'Exp', 'Salary', 'Type', 'Location'];
  selected: string ='Age';

  ngOnInit() {

  }

}
