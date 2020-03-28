import {Component, Input} from '@angular/core';
import {Bar} from '../../models/bar.class';

@Component({
  selector: 'app-bar',
  templateUrl: './bar.component.html',
  styleUrls: ['./bar.component.css']
})
export class BarComponent {

  @Input() data: Bar[];
  @Input() yAxisLabel: string;
  // view: any[] = [1100, 700];
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  trimYAxisTicks = false;
  xAxisLabel = 'Users';
  colorScheme = {
    domain: ['#ff9671', '#ffc75f', '#0089ba', '#ffd0ff', '#00c9a7', '#3b1c32', '#c4fcef', '#d4e09b', '#8d5b4c',
      '#c4bbaf', '#98d6ea', '#a6b1e1', '#d1cebd', '#75daad', '#ad62aa', '#f6eedf', '#a8d3da', '#eb9788', '#84142d',
      '#ffc7c7', '#ffae8f', '#f64b3c', '#72b5b7']
  };

}
