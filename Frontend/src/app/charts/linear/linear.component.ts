import {Component, Input} from '@angular/core';
import {Linear} from '../../models/linear.class';

@Component({
  selector: 'app-linear',
  templateUrl: './linear.component.html',
  styleUrls: ['./linear.component.css']
})
export class LinearComponent {

  // view: any[] = [1100, 700];

  @Input() data: Linear[];
  @Input() yAxisLabel: string;
  @Input() xAxisLabel: string;

  legend = true;
  animations = true;
  xAxis = true;
  yAxis = true;
  showYAxisLabel = true;
  showXAxisLabel = true;
  timeline = true;
  colorScheme = {
    domain: ['#ff9671', '#ffc75f', '#0089ba', '#ffd0ff', '#00c9a7', '#3b1c32', '#c4fcef', '#d4e09b', '#8d5b4c',
      '#c4bbaf', '#98d6ea', '#a6b1e1', '#d1cebd', '#75daad', '#ad62aa', '#f6eedf', '#a8d3da', '#eb9788', '#84142d',
      '#ffc7c7', '#ffae8f', '#f64b3c', '#72b5b7']
  };

}
