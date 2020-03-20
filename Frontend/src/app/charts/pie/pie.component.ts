import {Component, Input} from '@angular/core';
import {Pie} from '../../models/pie.class';

@Component({
  selector: 'app-pie',
  templateUrl: './pie.component.html',
  styleUrls: ['./pie.component.css']
})
export class PieComponent {

  @Input() data: Pie[];
  view: any[] = [1100, 700];
  gradient = false;
  showLegend = false;
  showLabels = true;
  isDoughnut = false;
  trimLabels = false;
  colorScheme = {
    domain: ['#ff9671', '#ffc75f', '#0089ba', '#ffd0ff', '#00c9a7', '#3b1c32', '#c4fcef', '#d4e09b', '#8d5b4c',
      '#c4bbaf', '#98d6ea', '#a6b1e1', '#d1cebd', '#75daad', '#ad62aa', '#f6eedf', '#a8d3da', '#eb9788', '#84142d',
      '#ffc7c7', '#ffae8f', '#f64b3c', '#72b5b7', '#deff8b']
  };

}
